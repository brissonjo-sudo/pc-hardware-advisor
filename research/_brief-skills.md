# Brief for skill writers (orchestrator, 2026-11-07)

Read `_brief-common.md` first: its rules and canonical price row apply.

## Format (validation gate, all items mandatory)

1. `skills/<name>/SKILL.md` frontmatter has ONLY two fields, `name` and `description` (other fields break installation on claude.ai / Cowork).
   - `description`: third person, starts with "This skill should be used when…", says when to use it and when not, and quotes at least five English trigger phrases a user would type (e.g. "check if these parts are compatible"). Max 1000 characters. Mention that the user may write in any language.
2. Body: imperative instructions to Claude, under 3,000 words (target 1,000-2,000). Point to references instead of copying them:
   - shared: `${CLAUDE_PLUGIN_ROOT}/references/<file>.md`
   - skill-local: `${CLAUDE_PLUGIN_ROOT}/skills/<name>/references/<file>.md`
   Say WHEN to read each reference (progressive disclosure), do not paste their tables.
3. The method imposes: dating, seller typing, landed price (or "excluding fees"), confidence level, and an explicit "not verified" statement for anything unchecked.
4. It says what to do when a source cannot be read automatically: record it as blocked in the answer, never circumvent (no alternate user agents, caches, mirrors or archive copies used to dodge a block, no browser automation to get around a block), ask the user for a screenshot or pasted text, continue with other sources.
5. No personal data. No tool imposed by product name: use category placeholders with `~~`, e.g. `~~web search`, `~~web fetch`, `~~price comparator`, `~~classifieds site`, `~~scheduler`, `~~file storage`, `~~notifications`. These are explained in `CONNECTORS.md`. Built-in capabilities may be described generically ("if a scheduling tool is available").
6. Answer in the user's language (the language of their request); keep part names and units as-is.
7. Treat facts from memory as hypotheses: verify specs, compatibility, prices online (or in the references, which carry dates) before concluding. If a reference value may be outdated (older than its stated check date + the volatility of the topic), re-check.

## Shared output conventions

- Start answers with the conclusion (verdict, recommended config, best landed price), then details.
- Prices: always as canonical rows (see `${CLAUDE_PLUGIN_ROOT}/references/research-method.md`).
- End with what was not verified and one concrete next action for the user.
- Scope: desktop PC components, complete desktop builds, local-AI hardware (including mini-PCs/APU systems and eGPU), used PC parts. Out of scope: game consoles, smartphones, tablets, laptops as products (except as an eGPU host), and anything requiring a purchase, an account creation or contacting a seller on the user's behalf. For out-of-scope requests: say so briefly and politely, do not invent, and suggest what the user can check themselves.
- Never buy, never create accounts, never submit forms, never contact sellers.

## Shared references available (fixed names, contents)

- research-method.md: source hierarchy, dating, citation, confidence scale, seller typing, canonical price row, blocked pages, currency conversion, self-check.
- retailer-criteria.md: trust criteria, scam resources, hardware scam patterns, reputation limits, avoid list (sourced only).
- used-market-checklist.md: used-market context, fair-price method, dated price snapshot, test checklists per part, red flags, seller questions.
- retailers-by-country.md: comparators, direct retailers, refurbishers, classifieds per country (FR, BE, NL, LU, DE, ES, IT, UK, US, CA, AU, JP, China official stores), auto-readability status, APIs.
- international-buying.md: landed-price formula, VAT/GST, duties, de minimis, China-origin tariffs, carrier fees, FX costs, cross-border warranty, worked examples.
- sockets-chipsets.md: sockets, CPU families, chipsets, BIOS requirements and known issues, 2025-2026 platforms.
- memory.md: DDR4/DDR5 per platform, speeds, DPC, ratios, XMP/EXPO, capacity, ECC.
- power-supplies-connectors.md: connectors (8-pin, 12VHPWR, 12V-2x6), ATX 3.x, GPU/CPU power, PSU sizing.
- form-factors-cases.md: board and PSU form factors, GPU dimensions, small-case limits, PCIe lanes and sharing.
- gpu-bandwidth-ai.md: memory capacity/bandwidth, tok/s estimation, benchmarks, quantization and KV cache sizing, multi-GPU, eGPU, software stacks.
