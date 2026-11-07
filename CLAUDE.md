# CLAUDE.md : pc-hardware-advisor

## Mémoire externe

Vault : `C:\Users\Krn\Documents\ClaudeMemory\02-Projects\pc-hardware-advisor\`
(overview, architecture, decisions, conventions, journal). Plan source : `plan-source.md` dans ce dossier du vault (hors dépôt).

## Spécifique au projet

- Plugin Claude Code / Cowork, contenu Markdown uniquement (skills, références, agent).
- Langue du paquet : anglais. Fichiers de pilotage (`DECISIONS.md`, `ORCHESTRATION.md`, `REPORT.md`) : français, sans tiret cadratin.
- Licence : PolyForm Noncommercial 1.0.0. Ne jamais écrire « open source » ni MIT.
- Dépendance des contrôles : `python -m pip install -r requirements-dev.txt` (PyYAML)
- Contrôler : `python scripts/check_content.py` (aussi en CI, `.github/workflows/checks.yml`)
- Valider : `claude plugin validate . --profile directory`
- Tester : `claude plugin eval . --eval-dir tests --no-publish --trust-plugin --judge-model sonnet`
- Construire : `python scripts/build_plugin.py` (exclut tests, research, pilotage)
- Branche par défaut : `main`

## À éviter

- Pousser sur GitHub tant que la visibilité du dépôt n'est pas confirmée par Jo.
- Inventer un prix, une API, une compatibilité : tout fait porte source et date.
- Données personnelles de Jo dans le paquet (ses machines vont dans `tests/` seulement).
