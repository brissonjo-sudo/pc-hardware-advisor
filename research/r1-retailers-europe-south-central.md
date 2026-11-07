# R1 Retailers: Germany, Spain, Italy
Collected: 2026-11-07 · Model: haiku · Method: WebFetch on homepages and search URLs (query "DDR5 6000 32GB") plus WebSearch for API/feed questions; no bypass of any block. Many domains returned 403/503/fetch errors or per-domain rate limits; those rows are recorded as blocked or unverified, not inferred.

Legend: Type = direct retailer / marketplace / professional refurbisher / private classifieds / comparator / manufacturer store. Auto-readable = yes / partial / blocked / unverified. Confidence = high / medium / low. Source numbers refer to ## Sources.

## Germany

| Name | URL | Type | Role | Auto-readable | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| Geizhals.de | https://geizhals.de/ | Comparator | Price comparison, shop names per offer (expected, not seen) | blocked (HTTP 403) | none official found; third-party scrapers and Shopify feed apps exist (not official) | Freshness and seller mixing not verified | low | [1], [30] |
| idealo.de | https://www.idealo.de/ | Comparator | Price comparison | blocked (fetch error, "unable to fetch") | Partner Web Service PWS 2.0 exists for merchants (secondary sources only) | Seller display and marketplace mixing not verified | low | [2], [31] |
| Billiger.de | https://www.billiger.de/ | Comparator | Price comparison | blocked (HTTP 403) | none found | Nothing else verified | low | [3] |
| Alternate.de | https://www.alternate.de/ | Direct retailer | Full PC parts range, first-party | partial (product list and prices readable; filters JS-loaded; "session timed out" notice; 684 results, only 24 visible) | none found | Appears to sell direct (no third-party labels seen) | medium | [5] |
| Mindfactory.de | https://www.mindfactory.de/ | Direct retailer | PC parts specialist | blocked (HTTP 403) | none found | Not verified as direct vs marketplace | low | [4] |
| Caseking.de | https://www.caseking.de/ | Direct retailer | PC parts and gaming hardware | blocked (HTTP 403) | none found | Homepage not fetched | low | [6] |
| Cyberport.de | https://www.cyberport.de/ | Direct retailer | PC parts and electronics | blocked (fetch error) | none found | Not verified | low | [7] |
| Notebooksbilliger.de | https://www.notebooksbilliger.de/ | Direct retailer | Notebooks and PC parts | blocked (HTTP 403) | none found | Not verified | low | [8] |
| Computeruniverse.net | https://www.computeruniverse.net/ | Direct retailer | PC parts and IT | blocked (fetch error) | none found | Not verified | low | [9] |
| Amazon.de | https://www.amazon.de/ | Marketplace (mixed Amazon direct + third-party) | Mass market | blocked (HTTP 503 on search URL; may be transient) | Amazon product-advertising API exists but requires affiliate account (not checked) | Seller type must be read per offer | low | [10] |
| Kleinanzeigen.de | https://www.kleinanzeigen.de/ | Private classifieds | Used PC components | yes (listings with title, price, location, date readable without login; 345 results, 335 private and 10 commercial per filter counts shown) | none found | Terms of use not read; robots status not stated in fetched text | medium | [11] |
| refurbed.de | https://www.refurbed.de/ | Professional refurbisher / marketplace | Refurbished goods marketplace (mixed refurbed first-party and third-party suppliers) | partial (text readable; no product listings captured; recommendations "not loading") | none found | No PC components (CPU/GPU/RAM) seen on the page; category list includes desktops and accessories only; discount claims inconsistent (40 % vs 70 %) | medium | [12] |

## Spain

| Name | URL | Type | Role | Auto-readable | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| idealo.es | https://www.idealo.es/ | Comparator | Price comparison | blocked (fetch error) | see idealo.de (PWS 2.0, secondary sources) | Not verified | low | [19] |
| Kelkoo.es | https://www.kelkoo.es/ | Comparator | Price comparison | unverified (per-domain safety check rate-limited, two attempts) | unknown | Freshness and seller mixing not verified | low | [16] |
| PcComponentes | https://www.pccomponentes.es/ | Direct retailer (marketplace share not checked) | Full PC parts range | partial/unverified (es search URL 301-redirects to http://www.pccomponentes.com/; target not fetched) | none found | Marketplace share not verified; site sells refurbished tiers (search snippet only, see Italy notes) | low | [14] |
| Coolmod.com | https://www.coolmod.com/ | Direct retailer | PC parts specialist | blocked (too many redirects) | none found | Not verified | low | [15] |
| LDLC.es (LDLC España) | https://www.ldlc.com/es-es/ | Direct retailer (first-party) | PC components: GPU, CPU, motherboard, RAM, SSD, PSU, PC configurator | partial (category names and product links readable; no prices in capture; "Se ha producido un error" banner) | none found | No marketplace seen | medium | [13] |
| Amazon.es | https://www.amazon.es/ | Marketplace (mixed) | Mass market | unverified (fetch result not reliably attributed in batch; retry needed) | Amazon PA-API requires affiliate account (not checked) | Seller type must be read per offer | low | [17] |
| Wallapop | https://es.wallapop.com/ | Private classifieds (plus Wallapop Pro business sellers) | Used goods | partial (homepage readable; no listings captured; "Cargando..." seen; login-required status unclear) | none found | Listings readability without login not confirmed | low | [18] |

## Italy

| Name | URL | Type | Role | Auto-readable | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| Trovaprezzi.it | https://www.trovaprezzi.it/ | Comparator | Price comparison | blocked (HTTP 403) | none found | Seller display and freshness not verified | low | [20] |
| idealo.it | https://www.idealo.it/ | Comparator | Price comparison | blocked (fetch error) | see idealo.de (PWS 2.0, secondary sources) | Not verified | low | [21] |
| Drako.it | https://www.drako.it/ | Direct retailer (single operator, Drako Legacy S.R.L.; two physical stores listed) | Gaming PCs, graphics cards, watercooling, components; "rivenditore autorizzato" | yes (product names and prices readable; e.g. DDR5 Corsair Vengeance 5200 MHz 16GB at 324,90 EUR, reduced to 309,90 EUR) | none found | Direct, no third-party sellers seen; PC component range narrower than generalists | medium | [26] |
| ePrice.it | https://www.eprice.it/ | Direct retailer (single operator, B2VIBE S.r.l. in footer) | Electronics incl. Informatica > Componenti | yes (product cards with name, brand, price, discount; page text complete) | none found | Attribution of this fetch to eprice is inferred from page content, not from a confirmed URL response | medium | [22] |
| Yeppon.it | https://www.yeppon.it/ | Direct retailer (not verified) | Not verified | unverified (HTTP 503 or 403 ambiguous in batch; retry needed) | none found | Not verified | low | [23] |
| Amazon.it | https://www.amazon.it/ | Marketplace (mixed) | Mass market | unverified (fetch result not reliably attributed in batch) | Amazon PA-API requires affiliate account (not checked) | Seller type must be read per offer | low | [24] |
| Subito.it | https://www.subito.it/annunci-italia/vendita/informatica/ | Private classifieds | Used computer items | unverified (per-domain safety check rate-limited, two attempts) | none found | Not verified | low | [25] |
| Back Market (IT) | https://www.backmarket.it/ | Professional refurbisher / marketplace | Refurbished goods | unverified (per-domain safety check rate-limited) | none found | Not verified | low | [27] |
| Messoanuovo.it | https://www.messoanuovo.it/ | Professional refurbisher | Refurbished computers, Italy | unverified (not fetched; name seen only in search results) | none found | Only search-snippet evidence | low | [30] |
| PcComponentes (IT storefront, /pages/ricondizionati) | https://www.pccomponentes.it/pages/ricondizionati | Direct retailer, refurbished tiers | Refurbished grades: as new 3 years, almost new 2 years, functional 1 year (per Tuttotech snippet) | unverified (search snippet only) | none found | Warranty figures are from a secondary article, not from the retailer page | low | [30] |

## Refurbishers and classifieds: German and Spanish coverage gaps

- Germany professional refurbishers beyond refurbed.de: not verified (Back Market DE rate-limited).
- Spain professional refurbishers: Back Market ES rate-limited; no other source verified.
- Italy classifieds: Subito.it rate-limited; no fetch succeeded.

## Not verified / gaps

- Geizhals, idealo (DE/ES/IT), Billiger, Trovaprezzi: all blocked (403 or fetch error). No freshness, seller display or marketplace-mix check possible. Do not bypass.
- Mindfactory, Caseking, Cyberport, Notebooksbilliger, Computeruniverse, Coolmod, Yeppon: blocked or not readable; marketplace share unknown.
- Amazon DE/ES/IT: results 503/403 or ambiguous; seller type must be determined per offer with an authenticated/affiliate source.
- PcComponentes marketplace share: not verified (redirect to .com not followed).
- Kelkoo.es, Subito.it, Back Market DE/ES/IT: rate-limited by the fetch safety checker; retry later in a new session.
- Official API/feed: none found for any retailer. For idealo, a PWS 2.0 partner API is referenced by third-party integrators (not verified against idealo's own docs). For Geizhals, no official partner API found; third-party scrapers exist (not endorsed).
- Confidence for ePrice and LDLC rows depends on single fetch results; treat as plausible until re-checked.
- Date checks: all fetches on 2026-11-07. Search-snippet claims are secondary and must be confirmed on the primary page.

## Sources

1. https://geizhals.de/?fs=DDR5+6000+32GB (403, 2026-11-07)
2. https://www.idealo.de/preisvergleich/MainSearchProductCategory.html?q=DDR5+6000+32GB (fetch error, 2026-11-07)
3. https://www.billiger.de/ (403, 2026-11-07)
4. https://www.mindfactory.de/search_result.php?search=DDR5+6000+32GB (403, 2026-11-07)
5. https://www.alternate.de/html/search.html?query=DDR5+6000+32GB (readable, partial, 2026-11-07)
6. https://www.caseking.de/ (403, 2026-11-07)
7. https://www.cyberport.de/ (fetch error, 2026-11-07)
8. https://www.notebooksbilliger.de/produkte/suche?q=DDR5+6000+32GB (403, 2026-11-07)
9. https://www.computeruniverse.net/de/search?q=DDR5+6000+32GB (fetch error, 2026-11-07)
10. https://www.amazon.de/s?k=DDR5+6000+32GB (503, 2026-11-07)
11. https://www.kleinanzeigen.de/s-pc-komponenten/k0 (readable, 2026-11-07)
12. https://www.refurbed.de/ (readable, partial, 2026-11-07)
13. https://www.ldlc.com/es-es/ (partial, error banner, 2026-11-07)
14. https://www.pccomponentes.es/buscar/?query=DDR5+6000+32GB (301 to http://www.pccomponentes.com/, not followed, 2026-11-07)
15. https://www.coolmod.com/buscar?q=DDR5+6000+32GB (too many redirects, 2026-11-07)
16. https://www.kelkoo.es/ (rate-limited, 2026-11-07)
17. https://www.amazon.es/s?k=DDR5+6000+32GB (unverified, 2026-11-07)
18. https://es.wallapop.com/ (partial, 2026-11-07)
19. https://www.idealo.es/ (fetch error, 2026-11-07)
20. https://www.trovaprezzi.it/ (403, 2026-11-07)
21. https://www.idealo.it/ (fetch error, 2026-11-07)
22. https://www.eprice.it/ (readable, attribution inferred, 2026-11-07)
23. https://www.yeppon.it/ (unverified, 2026-11-07)
24. https://www.amazon.it/s?k=DDR5+6000+32GB (unverified, 2026-11-07)
25. https://www.subito.it/annunci-italia/vendita/informatica/ (rate-limited, 2026-11-07)
26. https://www.drako.it/ (readable, 2026-11-07)
27. https://www.backmarket.it/ , https://www.backmarket.de/ , https://www.backmarket.es/ (rate-limited, 2026-11-07)
28. https://www.geizhals.de (WebSearch, 2026-11-07): search surfaced third-party scrapers https://readme.priceapi.com/reference/geizhals-1 and https://www.xcrawl.com/de/solutions/geizhalsde-price-comparison-scraper-api; no official API found.
29. https://apps.shopify.com/geizhals-sync?locale=de (WebSearch, 2026-11-07): third-party feed app, not official.
30. https://www.refurb.me/it/refurbishers and https://www.roxmir.it/guide/computer-ricondizionati-guida-completa-2025/ (WebSearch snippets, 2026-11-07): secondary guides, not primary evidence.
31. https://help.productsup.com/en/29544-30186-add-idealo-partner-api-v2-0-export.html and https://www.mergado.com/integration/idealo-csv.md (WebSearch, 2026-11-07): secondary descriptions of idealo PWS 2.0 and CSV feed (CSV/TXT/XML, hosted URL/FTP/HTTP, roughly every 30 minutes); verify on import.idealo.com.
