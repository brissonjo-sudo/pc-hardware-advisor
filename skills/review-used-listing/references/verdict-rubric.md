# Verdict rubric for used listings

Last checked: 2026-11-07. Values change: verify online before concluding.

Project policy for scoring a used listing. Thresholds below are plugin rules (inference, not sourced external facts): adjust them with judgement and say so. Evidence details come from `${CLAUDE_PLUGIN_ROOT}/references/used-market-checklist.md` and `${CLAUDE_PLUGIN_ROOT}/references/retailer-criteria.md`.

## 1. Hard "avoid" triggers

Any one gives `avoid`, whatever the price:
1. Payment requested off-platform, by bank transfer to an unknown seller, as a deposit, or as "friends and family".
2. Seller refuses an in-person test or a test on the user's own bench, or any return window on a shipped item.
3. Identity mismatch: model, VRAM size or type, or serial in photos or test capture differs from the listing or the official spec.
4. Test screenshot clearly unrelated to the item (no serial, no date, different handle, different model).
5. "For parts", "untested" or "not working" sold at a working-unit price.
6. Price under about 60% of the recent sold range with at least one more red flag (stock photos, new profile, pressure). The 60% figure echoes a single low-quality source for SSDs; treat as heuristic.
7. PSU of unknown age or history bought for a high-value system: recommend new instead.

## 2. Scoring grid

Score each row: +1 favourable, 0 neutral or not shown, -1 unfavourable. Write "not shown" rather than guessing. Count one fact once: a missing receipt scores -1 in Proof only, and Warranty is then 0 unless the seller states there is no warranty or it is not transferable.

| Row | +1 | 0 | -1 |
|---|---|---|---|
| Price vs recent sold range (60 days, same region, sample 10 or more) | At or below the range | Within the range, or data below 10 items | Above the range |
| Market data quality | Sold data, dated, 10 or more items | Asking data, labelled | None verifiable |
| Identity | Serial and variant confirmed by photos | Partly shown | Ambiguous or mismatched |
| Proof | Receipt, box, matching serial | Some | None |
| Warranty | Written, transferable, verified remaining | Claimed only | None or non-transferable |
| Seller profile | History and reviews on more than one source | Thin | New or empty |
| Handover | Live test before payment, or protected shipping with a return window | Test possible, details open | Unclear |
| Condition and use history | Light home use, clean | Unknown | Mining/heavy use with wear signs, opened or flashed without disclosure |

Reading (plugin rule):
- No hard trigger and total 5 or more, price within or below range: `grab it`, conditional on passing the handover tests.
- No hard trigger and total 0 to 4, or price above range: `negotiate`.
- Total below 0, or two or more rows at -1 on identity, handover, price: `avoid`.
- Market not verified: cap at `negotiate`.

## 3. Negotiation levers

Use only levers backed by evidence from this listing. Never invent a defect.
- **Market evidence**: dated sold prices (not asking) from the review. Quote source, date, sample size. This is the strongest lever; without it, do not name a number.
- **Age and wear**: purchase date, fan noise, dust, pad and paste age, cosmetic damage, high hotspot or memory-junction temperature at the test.
- **Missing box or invoice**: no proof of purchase, no accessories, no cable set.
- **Warranty remaining**: none, expired, or non-transferable. Price at zero value unless written proof.
- **Refurbishment cost**: repaste and pads, roughly 20-40 USD per the checklist's low-quality source; replacement fan; new PSU cable.
- **Logistics**: pickup and in-person test, cash on the spot, several parts bought together, shipping or platform fees absorbed.

How to present: opening offer = justified low end of the evidence; target = middle; walk-away = top of the recent sold range minus the value of missing proof. Label the figures "suggested, argued from <evidence>, <date>".

## 4. Seller question bank by part type

Pick the ones that matter; ask all of them only for high-value items. Common to all parts:
- Purchase date and proof of purchase? Original box and accessories?
- Reason for selling? How long used, for what workload?
- Any repairs, repaste, repad, BIOS flash, overclock, or water damage?
- Live test allowed before payment? Return window if shipped?
- Pickup in a public place? Payment only through the platform's protected method?

**GPU**
- Mining, rendering or AI use? Hours per day if known.
- Which BIOS version? Dual-BIOS switch position?
- Photos of serial sticker, backplate, fans, PCIe connector and power sockets?
- Any artifacts, crashes, fan noise?

**CPU**
- Which motherboard and BIOS did it run on? Overclocked, undervolted, delidded?
- Photos of the pins (AM4/AM5) or pads and the IHS?

**RAM**
- Exact part number and running speed/voltage?
- Ever overclocked or manually tuned? Tested with a bootable memory test?

**SSD**
- Capacity as seen by the OS? SMART screenshot with power-on hours and total written?
- Used as boot, cache, server or mining/plotting drive?

**Motherboard**
- BIOS version, CPU and memory it ran with? Any POST codes, bent pins, damaged slots?
- Photos of the CPU socket, VRM heatsinks, rear I/O and slots? Back-panel shield and accessories?

**PSU**
- Purchase date, model and wattage label, serial photo?
- Hours and load (always-on, mining, high-load gaming)? Fan noise, coil whine, shutdowns?

## 5. Message template (the user sends it)

Neutral wording. Adapt the bracketed parts. Claude drafts it; the user decides whether and how to send it.

> Hello, I am interested in your [item and variant] listed on [date]. Is it still available?
> Could you confirm: [2-4 questions from section 4]?
> I would like to test it before paying (for example [test relevant to the part]), in a public place or on my PC, and pay only through [platform protected method / cash on the spot after the test].
> Based on recent sold prices I found ([range, source, date]), would you accept [offer]?
> Thank you.

## Not verified

- Thresholds in sections 1-2 (60%, score cut-offs) are plugin heuristics, not external facts.
- Consumer-law rights against private sellers per country: not researched. Check an official source for the buyer's country.
