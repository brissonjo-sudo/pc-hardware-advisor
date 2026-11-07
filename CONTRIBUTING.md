# Contributing to PC Hardware Advisor

This project is licensed under the PolyForm Noncommercial License 1.0.0 (SPDX: PolyForm-Noncommercial-1.0.0). See [LICENSE](LICENSE).

## Contribution terms

By submitting a contribution (a pull request, a patch, data, text, translations or any other material), the contributor:

1. **Certifies** that they are its author, or that they have the right to submit it under these terms.
2. **Assigns** to the project author (Jo, GitHub: brissonjo-sudo) all rights in the contribution, including for commercial use and for future relicensing under any terms. Where assignment is not possible under applicable law, the contributor instead grants the project author a perpetual, worldwide, irrevocable, royalty-free, sublicensable license to all rights in the contribution, including for commercial use and for future relicensing under any terms.

A contribution is accepted only if the pull request description contains this exact sentence:

> I accept the contribution terms in CONTRIBUTING.md.

Pull requests without it are not reviewed.

This is not legal advice; these terms were written for the project and have not been reviewed by a lawyer. If you are unsure about your right to submit something (for example work done for an employer), ask before submitting.

## What makes a good contribution

- **Dated, sourced data.** Every fact in `references/` carries a source and a "last checked" date. A claim without both will be asked for them.
- **New country rows.** Retailers, comparators, classifieds sites, VAT and import rules for a country missing from `references/retailers-by-country.md` and `references/international-buying.md` are the most useful addition. Follow the existing row format and the criteria in `references/retailer-criteria.md`.
- **Corrected rates.** Fixes to VAT, duty or de minimis figures must cite the official source (tax or customs authority, official journal). Press articles are not enough.
- **Corrected specs and compatibility rules.** Cite the manufacturer page or datasheet.
- **Skill behavior fixes.** Describe the request that went wrong and what Claude should have done. Add or update an eval case under `tests/cases` when it applies.
- **Nothing that circumvents a site.** Contributions that work around a block (alternate user agents, caches, mirrors, scraping behind logins) are declined.
- **Nothing that buys or contacts.** The plugin is read-only by design.

## Style

- Write in **English**, in the imperative ("Check the socket", not "You should check the socket").
- Keep it short. One rule, one place.
- **No personal data**: no names, addresses, account identifiers, or private listing details. Use anonymized or invented placeholders in examples.
- Refer to tools **by category** with the `~~` placeholder (for example `~~web search`, `~~web fetch`, `~~scheduler`), never by product. New categories go in [CONNECTORS.md](CONNECTORS.md).
- Date every figure and name its source.
- Describe the project only as source-available under a noncommercial license.

## Validate and test

From the repository root, install the check dependency, then run the content checks and the build (these two also run in CI on every push and pull request):

```
python -m pip install -r requirements-dev.txt
python scripts/check_content.py
python scripts/build_plugin.py
```

Validate the plugin structure with Claude Code:

```
claude plugin validate . --profile directory
```

Run the eval suite (manual only: it runs real Claude sessions, needs your own Claude Code login and costs usage, so CI does not run it):

```
claude plugin eval . --eval-dir tests --no-publish --trust-plugin --judge-model sonnet
```

The checks, the build and the validation should pass before you open a pull request. Say in the description whether you ran the eval suite and its scores.

## Commits

Use [Conventional Commits](https://www.conventionalcommits.org/): `type(scope): summary`, with types such as `feat`, `fix`, `docs`, `refactor`, `test`, `chore`. Examples: `docs(references): add Poland retailers`, `fix(check-compatibility): correct AM5 cooler condition`. Keep each commit to one logical change.

## Pull requests

1. Describe what changed and why, and cite sources for data changes.
2. Add the acceptance sentence from "Contribution terms" above.
3. Update [CHANGELOG.md](CHANGELOG.md) under "Unreleased".
