# DECISIONS : pc-hardware-advisor

Décisions prises seul en cours de mission, avec leur raison. Jamais réécrites : une décision remplacée reçoit une nouvelle entrée qui la supersede.

| # | Date | Décision | Raison |
|---|---|---|---|
| D1 | 2026-11-07 | Projet créé dans `E:\Claude code\Projects\pc-hardware-advisor`. | Le dossier « Projet » n'existe pas ; `Projects` est la racine de tous les dépôts de Jo. |
| D2 | 2026-11-07 | Aucune poussée vers GitHub sans accord explicite de Jo. | Le dépôt `brissonjo-sudo/pc-hardware-advisor` existe déjà, vide, mais **public**. Pousser = publication publique, interdite par le plan (§8). Question posée à Jo en fin de mission : passer le dépôt en privé puis pousser. |
| D3 | 2026-11-07 | `LICENSE` = texte du fichier `PolyForm-Noncommercial-1.0.0.md` du dépôt officiel `polyformproject/polyform-licenses`. | La page polyformproject.org est en HTML ; le texte du dépôt officiel a été comparé mot à mot à la page : identique hors menu du site. |
| D4 | 2026-11-07 | La synthèse Sonnet de la phase R est fusionnée avec la rédaction des références (phase 1). | Évite une couche intermédiaire qui recopierait `research/` ; le rédacteur Sonnet lit directement les relevés. |
| D5 | 2026-11-07 | Recherche par grappes de pays (4 agents) au lieu d'un agent par pays (11). | Même brief, moins de surcoût de contexte ; la couverture par pays est contrôlée à la validation. |
| D6 | 2026-11-07 | Sonnet (et non Haiku) pour la recherche technique R4 et les règles fiscales R2. | Risque principal du plan : une valeur fausse (socket, bande passante, seuil douanier). Haiku reste sur la lecture de sites. |
| D7 | 2026-11-07 | Auteur dans `plugin.json` : nom et profil GitHub, sans courriel. | Règle « aucune donnée personnelle dans le paquet ». |
| D8 | 2026-11-07 | Banc de test = `claude plugin eval --eval-dir tests` (cas dans `tests/cases/`, résultats dans `tests/results/`). | Outil officiel disponible (Claude Code 2.1.310), arborescence identique au plan. |
| D9 | 2026-11-07 | Nom « pc-hardware-advisor » : un dépôt homonyme existe (`capybara114/pc-hardware-advisor`, site web chinois, pas un plugin Claude) ; aucun plugin de ce nom dans la marketplace officielle `claude-plugins-official`. Nom conservé. | Pas de conflit dans l'écosystème des plugins Claude ; homonymie GitHub sans portée de marque connue (non vérifié auprès d'un registre de marques). |
| D10 | 2026-11-07 | Périmètre : composants PC de bureau, configurations de bureau, matériel d'IA locale (dont mini-PC à APU et eGPU), pièces d'occasion. Hors périmètre : consoles, smartphones, tablettes, portables comme produits (sauf hôte d'eGPU). | Le plan cite consoles et smartphones comme hors périmètre ; les portables ne sont pas couverts par la recherche (aucune donnée vérifiée). |
| D11 | 2026-11-07 | Outils cités par catégories avec la convention Cowork `~~catégorie` (`~~web search`, `~~scheduler`…), expliquées dans `CONNECTORS.md`. | Convention documentée du format Cowork pour les plugins partagés hors organisation ; répond à la règle « aucun outil imposé ». |
| D12 | 2026-11-07 | Frontmatter des skills limité à `name` et `description`. | Hors Claude Code (claude.ai, API Skills), les autres champs provoquent une erreur à l'installation (doc code.claude.com/docs/en/skills.md). |
| D13 | 2026-11-07 | Les skills citent les références par `${CLAUDE_PLUGIN_ROOT}/...`. | Variable substituée dans le corps des skills de plugin (doc officielle) ; un chemin relatif `../../` n'est pas documenté. |
| D14 | 2026-11-07 | Icône 512 px dessinée par script (`scripts/make_icon.py`), sans ressource externe. | Lève l'avertissement ICON_MISSING du validateur ; aucun droit tiers. |
