<!-- language-bar -->
**English** · [Français](docs/README.fr.md) · [Español](docs/README.es.md) · [Deutsch](docs/README.de.md) · [Português](docs/README.pt.md) · [简体中文](docs/README.zh-CN.md) · [日本語](docs/README.ja.md) · [हिन्दी](docs/README.hi.md) · [العربية](docs/README.ar.md)
<!-- /language-bar -->

# PC Hardware Advisor

PC Hardware Advisor is a plugin for Claude (Claude Code, and Cowork in the Claude desktop app) that makes Claude dependable on desktop PC hardware. It finds the best delivered price for a part anywhere in the world, checks that parts work together, designs complete builds for a use and a budget, sizes machines for local AI, judges second-hand listings, and watches prices on a schedule. Every figure it gives is dated, sourced and graded for confidence, and the plugin only reads: it never buys anything and never contacts a seller.

Claude answers in the language you write in. Part names, SKUs and units stay as published.

## What it does

Six skills and one sub-agent.

- **`hunt-prices`**: finds the best landed price (delivered, with VAT, duties and shipping) for one exact item, worldwide. Direct retailers come first, marketplaces are listed separately, and each row carries a confidence column. It uses the `price-scout` agent to read several sites in parallel.
- **`check-compatibility`**: gives pairwise verdicts between parts: compatible, compatible with conditions, or incompatible. A conditional verdict states the exact condition and the source.
- **`build-config`**: designs a complete build from the use, the budget, the country and your constraints. It returns a main build plus a cheaper and a stronger variant. It proposes new parts and professionally refurbished ones only.
- **`size-local-ai`**: sizes hardware for running models locally. It covers VRAM, memory bandwidth, tokens-per-second estimates (labelled as estimates), multi-GPU, APUs, eGPUs and software stacks.
- **`review-used-listing`**: reviews one second-hand listing and returns a verdict: grab it, negotiate, or avoid. It adds questions for the seller, tests to run at handover, and a negotiation margin.
- **`track-price`**: sets up scheduled re-checks of a price, alerts you only when it falls below your threshold, and keeps a history file. It never buys.
- **`price-scout`** (agent): reads several retailer or marketplace pages for one exact part and returns normalized price rows, with no analysis. `hunt-prices` launches it.

Out of scope: consoles, smartphones, tablets, laptops as products, and anything that buys or contacts sellers.

## Principles

- **Every price is dated.** A price without a read date is not reported.
- **The seller is typed.** Direct retailer, marketplace seller, refurbisher or private individual are different rows, never mixed.
- **Landed price, or "excluding fees".** Prices include VAT, duties and shipping to your country. When a component cannot be established, the row says "excluding fees" instead of guessing.
- **Confidence is shown.** Each figure says how well it is supported.
- **Nothing is invented.** If a spec, a price or a rule cannot be sourced, Claude says so.
- **Blocked sites: browser fallback, never tricks.** If a site refuses automated reading and a browser tool is available, Claude offers in one line to open the page in your browser; reply "yes" and it reads the few pages that matter, read-only, and says so. It stops at any captcha or bot check and never imitates a human to pass one. Otherwise it asks you for a screenshot or pasted text. No alternate user agents, caches or mirrors are used.
- **Read-only.** The plugin never buys, never creates accounts, never submits forms and never contacts sellers. You do that yourself.

Ten shared references (research method, retailers by country, retailer criteria, international buying, used-market checklist, sockets and chipsets, memory, power supplies and connectors, form factors and cases, GPU bandwidth for AI) are dated and sourced. They were last checked on 2026-11-07.

## Installation

### Claude Code

Use the repository as a marketplace, then install the plugin from it.

```
claude plugin marketplace add <owner/repo or local path>
claude plugin install pc-hardware-advisor@pc-hardware-advisor
```

`marketplace add` accepts a GitHub repository (`owner/repo`), a git or https URL, or a local path. For this repository, the GitHub address is `brissonjo-sudo/pc-hardware-advisor`. Add `--scope project` or `--scope local` to either command if you do not want a user-wide install (the default is `user`).

Check what is installed with `claude plugin marketplace list`.

### Local development

To try the plugin from a working copy without installing it:

```
claude --plugin-dir <path to this repository>
```

### Claude desktop / Cowork

Get the `pc-hardware-advisor.plugin` file (attached to a release when one is published, or built from a working copy with `python scripts/build_plugin.py`, which writes it to `dist/`), drag it into the Claude desktop app, and accept the installation prompt.

## Update, verify and uninstall

**Update (Claude Code).** Refresh the marketplace, then update the plugin, then restart Claude Code:

```
claude plugin marketplace update pc-hardware-advisor
claude plugin update pc-hardware-advisor@pc-hardware-advisor
```

An update is offered only when the `version` in `plugin.json` changes.

**Verify.** Ask Claude "which plugin skills do you have for PC hardware?", or run `claude plugin list` and look for `pc-hardware-advisor` and its version.

**Uninstall.** Run `claude plugin uninstall pc-hardware-advisor@pc-hardware-advisor`. In the Claude desktop app, remove the plugin from the plugins settings. Price-history files you created stay where you put them.

The repository is currently private, so the marketplace route works only for accounts with access to it; the `.plugin` file is the alternative.

## Example requests

Claude picks the right skill from the request. A few examples:

1. "Find the best delivered price to Germany for a Ryzen 7 9800X3D. Direct retailers first, marketplaces separately."
2. "Is it cheaper to import an RTX 5070 Ti from the US to Canada once duties and shipping are included?"
3. "Will this DDR5-6000 kit work with an ASUS TUF B650 board and a Ryzen 7 7700? Give a verdict per pair."
4. "Build me a quiet 1440p gaming PC for 1,400 EUR in Spain. Give me a cheaper and a stronger variant too."
5. "I want to run a 70B model locally at a usable speed. What VRAM and memory bandwidth do I need, and would two used 24 GB GPUs do it?"
6. "Check this used RTX 3090 listing for me (link below). Grab it, negotiate, or avoid? What should I ask the seller?"
7. "Watch the price of the Samsung 990 Pro 2 TB in the UK and alert me only if it goes under 120 GBP."
8. En français : "Trouve-moi le meilleur prix livré en France pour une alimentation 850 W ATX 3.1, vendeurs directs d'abord, places de marché à part."
9. En español: "Quiero montar un PC para edición de vídeo con 1.800 EUR en España. ¿Qué configuración me recomiendas, y qué compatibilidad debo vigilar entre placa, RAM y GPU?"
10. "Can an APU with 64 GB of unified memory run a 32B model, and what speed should I expect? Label what is an estimate."

## Connectors

Skills refer to tools by category (web search, web fetch, price comparator, classifieds site, browser, scheduler, notifications), not by product, so any equivalent tool works. Nothing in the plugin requires an account, an API key or a paid service. Categories, optional data sources and the rules that apply to every tool are in [CONNECTORS.md](CONNECTORS.md).

## Limits

- **Prices are perishable.** A price is true at its read date only. Stock and promotions change within hours.
- **Some sites block automated reading.** Those rows are marked blocked, and Claude asks you for a screenshot or pasted text.
- **Tax and tariff rules are volatile.** VAT, customs duties and de minimis thresholds changed repeatedly in 2025 and 2026. Check the official source before a large import.
- **Estimates are estimates.** Tokens-per-second figures and similar projections are modelled, not measured on your machine, and are labelled as such.
- **Research coverage has gaps.** Some countries, retailers and niche parts are covered thinly. The references say where.
- **Use high effort.** In maintainer tests, `build-config` at medium effort read fewer retailers and missed cheaper options. Choose high effort in your app before asking for a build or a price hunt.
- **Not financial or legal advice.** The plugin informs a purchase decision. It does not advise on tax, customs or consumer-law matters.

## Privacy

The plugin itself collects nothing and sends nothing anywhere. Price histories written by `track-price` stay where you choose to keep them. The tools Claude uses to search and read pages (web search, web fetch, scheduler) follow their own providers' terms and privacy policies.

## Translations

Machine translations of this README, not reviewed by a human: [docs/README.fr.md](docs/README.fr.md), [docs/README.es.md](docs/README.es.md), [docs/README.zh-CN.md](docs/README.zh-CN.md), [docs/README.hi.md](docs/README.hi.md), [docs/README.pt.md](docs/README.pt.md), [docs/README.ar.md](docs/README.ar.md), [docs/README.de.md](docs/README.de.md), [docs/README.ja.md](docs/README.ja.md). The English version prevails.

## Contributing

Contributions are welcome under specific terms, including a rights assignment. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

PC Hardware Advisor is source-available under the PolyForm Noncommercial License 1.0.0 (SPDX: PolyForm-Noncommercial-1.0.0). Noncommercial use is permitted for everyone; commercial use requires a separate license from the author. The same license covers the skills, references, documentation and translations.

Full text: [LICENSE](LICENSE) and <https://polyformproject.org/licenses/noncommercial/1.0.0>.
