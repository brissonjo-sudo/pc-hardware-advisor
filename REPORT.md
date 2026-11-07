# REPORT : pc-hardware-advisor v0.1.0

Rapport de fin de mission. Rédigé le 2026-11-07 par l'orchestrateur (session principale). Plan source : `02-Projects/pc-hardware-advisor/plan-source.md` du vault.

## 1. Ce qui a été livré

| Livrable | Emplacement | État |
|---|---|---|
| Paquet installable | `dist/pc-hardware-advisor.plugin` (zip, 39 fichiers) | construit par `scripts/build_plugin.py`, contenu extrait validé par `claude plugin validate --profile directory --strict` |
| Manifeste | `.claude-plugin/plugin.json` (v0.1.0, licence SPDX), `marketplace.json`, `icon.png` | validé |
| 6 skills | `skills/build-config`, `check-compatibility`, `hunt-prices`, `size-local-ai`, `review-used-listing`, `track-price` (chacun avec `references/` propre) | relus par Opus, porte §7 validée (voir `ORCHESTRATION.md`) |
| Agent | `agents/price-scout.md` (Haiku, sortie en lignes de prix normalisées) | validé |
| 10 références partagées | `references/` (datées 2026-11-07, sourcées, section « Not verified ») | contrôle mécanique `scripts/check_content.py` réussi |
| Documentation | `README.md`, 8 traductions `docs/README.*.md`, `CONNECTORS.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `LICENSE` (texte officiel intégral) | contrôlée |
| Recherche | `research/` (10 relevés + 2 compléments AMD, briefs communs) | hors paquet |
| Tests | `tests/cases/` (7 cas `claude plugin eval`), `tests/results/*.md` (résumés commentés) | voir §2 |
| Pilotage | `DECISIONS.md` (D1 à D20), `ORCHESTRATION.md`, ce rapport | hors paquet |
| Mémoire | vault `02-Projects/pc-hardware-advisor/`, MOC mis à jour, index Graphify `graphify-out/` (661 nœuds, 866 arêtes, 62 communautés, `GRAPH_REPORT.md`, `graph.html`) | contrôle d'intégrité non disponible dans la version installée (D21) |

## 2. Résultats des sept tests

Banc : `claude plugin eval` (sessions Sonnet, juge Sonnet, seuil 0,8 par cas), accès web réel. Sept passages au total (`tests/results/run*.md`).

Scores par cas et par exécution (seuil 0,8 ; « - » = cas non relancé) :

| Cas | Skill visé | P1 | P2 | P3 | P4 | P5 | P6 (x2) | P7 | Au seuil |
|---|---|---|---|---|---|---|---|---|---|
| 01 Machine IA mini-ITX 14700KF + 3090 (FR) | build-config, check-compatibility, size-local-ai | 0,83 | 0,75 | 0,83 | - | 0,67 | 0,83 / 0,83 | 0,83 | 5 sur 7 |
| 02 Jeu AM5, kit XMP 7200 (EN) | check-compatibility | 1,00 | - | - | - | 1,00 | - | 1,00 | 3 sur 3 |
| 03 Kit DDR5 meilleur prix (FR) | hunt-prices, price-scout | 0,30 | 0,50 | 0,50 | 0,70 | 0,50 | 0,50 / 0,50 | 0,80 | 1 sur 8 |
| 04 Annonce RTX 3090 à 900 € (ES) | review-used-listing | 1,00 | - | - | - | 1,00 | - | 1,00 | 3 sur 3 |
| 05 Suivi 3090 sous 800 € (FR) | track-price | 0,50 | 0,88 | 0,88 | - | 0,88 | - | 0,25 | 3 sur 5 |
| 06 IA 32 Go, 2 000 €, monde entier (EN) | build-config, hunt-prices, size-local-ai | 0,60 | 0,40 | 0,60 | 0,60 | 0,40 | 0,60 / 0,60 | 0,60 | 0 sur 8 |
| 07 Hors périmètre (FR) | aucun | 1,00 | - | - | - | 1,00 | - | 0,50 | 2 sur 3 |

**Critère de fin du plan non atteint en totalité** : les sept cas n'ont pas réussi dans un même passage. Six cas sur sept ont atteint le seuil au moins une fois ; le cas 06 jamais. Boucle arrêtée après 7 passages et 4 séries de corrections, par décision de l'orchestrateur (rendement décroissant, variance du web du jour), et signalée ici plutôt que masquée.

Causes identifiées des échecs restants :
- 06 : les sources d'import hors UE lisibles manquent (Newegg et B&H en 403), donc pas de prix rendu d'import calculé sur une page réelle ; types de vendeur souvent non affichés sur les fiches françaises.
- 05 (P7) : quand l'environnement propose un planificateur **cloud** (routine persistante sur le compte), le modèle demande une confirmation avant de créer la tâche. Comportement prudent, défendable, mais contraire au correcteur. À trancher par Jo : créer directement ou confirmer d'abord ?
- 07 (P7) : aucun skill du plugin ne se déclenche (voulu) ; c'est Claude de base qui répond, avec des prix approximatifs. Le plugin ne contrôle pas ce cas sans intercepter toute question d'achat, ce qui serait pire.

Corrections apportées entre les passages (détail dans `tests/results/run*.md`) : lecture obligatoire des fiches produit, couverture minimale avant arrêt, typage du vendeur depuis la référence pays, affichage compact à colonnes obligatoires, pas de blocage sur des questions quand l'essentiel est fourni, aucun emplacement de configuration laissé vide, calcul obligatoire du prix rendu d'un prix étranger, historique de suivi toujours initialisé.

Lecture honnête :
- Les cas 02 (compatibilité AM5 + kit XMP 7200), 04 (annonce d'occasion en espagnol) et 07 (hors périmètre) ont réussi à chaque passage.
- Les cas qui lisent des prix réels (01, 03, 06) dépendent du web du jour : sites bloqués, pages sans ligne « vendu par ». Leur score varie d'un passage à l'autre ; les corrections ont porté sur des défauts reproductibles, pas sur le bruit.
- Constat de fond utile à Jo : aux prix de novembre 2026, 32 Go de DDR5 coûtent environ 530 à 700 € en France ; une machine neuve à 32 Go de VRAM n'entre pas dans 2 000 € (cas 06 : seule piste proche, un mini-PC Ryzen AI Max+ 395 128 Go, prix et configuration à confirmer).
- Critères transverses du plan : aucune valeur sans source ni date dans les réponses relues ; aucune marketplace présentée comme vendeur direct ; incertitudes explicites ; langue de la requête respectée (français, anglais, espagnol : correcteur « language » réussi à tous les passages).

## 3. Décisions prises seul (extrait de DECISIONS.md)

- D1 : projet dans `Projects\pc-hardware-advisor` (le dossier « Projet » n'existe pas).
- D2 puis D19 : poussée bloquée tant que le dépôt était public ; levée quand Jo l'a passé en privé (vérifié).
- D4, D5, D6 : synthèse fusionnée avec la rédaction des références ; recherche par grappes de pays ; Sonnet pour les faits techniques et fiscaux.
- D11, D12, D13 : outils par catégories `~~` ; frontmatter des skills limité à `name` et `description` (compatibilité claude.ai et Cowork) ; chemins `${CLAUDE_PLUGIN_ROOT}`.
- D15 : vérification mécanique par script plutôt que par un agent Haiku.
- D16 : amd.com illisible en lecture automatique ; données AMD prises chez ASUS et Sapphire, confiance abaissée.
- D17 : aucun outil de tâche planifiée persistante pendant les tests (planificateur de session uniquement).
- D20 : correcteur « prices » aligné sur la règle d'honnêteté du plan (type de vendeur « non confirmé » accepté s'il n'est jamais classé comme direct).

## 4. Sources jugées fiables et sources écartées

Fiables (lues en entier, confiance haute) : pages produit et spécifications Intel (ARK, article 000102331 sur l'instabilité Vmin), NVIDIA (fiches 30, 40 et 50), Intel ATX 3.1 Design Guide, ASUS (listes de processeurs supportés AM4 et AM5, réglage XMP sur AM5), Sapphire (puissance et dimensions Radeon), EUR-Lex (directives 98/6, 2011/83, 2019/771), CBP, USITC, gov.uk Trade Tariff, BCE et Frankfurter pour les taux de change, tableaux de mesures llama.cpp.

Écartées ou dégradées :
- PCPartPicker et TechPowerUp : conditions d'utilisation et robots.txt interdisent l'accès automatisé (non cités comme outils).
- Amazon Product Advertising API : retirée ; eBay Marketplace Insights : accès restreint ; Newegg, Idealo, Google Merchant : API réservées aux marchands.
- amd.com : expirations systématiques (non contourné) ; Geizhals, idealo, plusieurs Amazon : blocages 403.
- Blogs et presse : utilisés en confiance moyenne pour les mesures (eGPU, double 3090) et le point DDR5-6000 sur AM5 (source de presse 2022 relayant AMD).

## 5. Limites connues et pistes pour la v0.2

- **Déclenchement de `track-price`** (passages 8 à 10, décision D22) : avec sa description d'origine, une demande formulée surtout comme une planification était prise par le skill intégré de routines planifiées (ni relevé initial ni historique). Après renforcement de la description (et correction d'une erreur YAML détectée au passage), `track-price` est déclenché 2 fois sur 2 au passage 10 (scores 1,00 et 0,25). Contournement si besoin : nommer le skill (« utilise track-price »). Non testé dans Cowork.
- **Frontmatters** : trois descriptions (`hunt-prices`, `track-price`, agent `price-scout`) n'étaient pas du YAML strictement valide (tolérées par Claude Code, risque de rejet dans claude.ai ou Cowork). Corrigé ; le script de contrôle utilise désormais un vrai analyseur YAML.

- Couverture : des dizaines de sites marqués « not tested (rate limit) » à cause du parallélisme de la phase R ; repasse séquentielle à prévoir. Luxembourg et données d'occasion européennes faibles.
- Données AMD : tableaux de chipsets, nombre de lignes PCIe et AGESA par processeur non lus sur amd.com.
- Règles fiscales volatiles : exclusions Section 301 américaines expirant le 2026-11-09, suppression annoncée du seuil britannique de 135 GBP, droit forfaitaire européen de 3 € jusqu'en 2028 : à revérifier à chaque version.
- Variance des tests à prix réels : passer à `--runs 3` et à une suite de cas « hors ligne » (pages fournies en capture) pour isoler le comportement du skill du web du jour.
- Pistes : connecteur comparateur de prix par catégorie, API à clé utilisateur (eBay Browse, Keepa), nouvelles zones (Pologne, pays nordiques, Corée, Inde), mode « capture d'écran d'abord » pour les sites bloqués.

## 6. Consommation par phase et par modèle

Jetons des sous-agents (relevés en fin de tâche) :

| Phase | Modèle | Agents | Jetons |
|---|---|---|---|
| R recherche | Haiku | 7 (4 zones, critères, occasion, complément Radeon) | 1 013 837 |
| R recherche | Sonnet | 6 (API, achat international, plateformes, alimentation et formats, GPU et IA, complément AMD) | 1 102 829 |
| 0 vérification doc | (guide Claude Code) | 1 | 112 166 |
| 1 références | Sonnet | 5 | 746 858 |
| 2 à 4 skills et agent | Sonnet | 6 (dont référence GPU et IA) | 873 720 |
| 5 README, CONTRIBUTING, CHANGELOG | Sonnet | 1 | 118 443 |
| 5 traductions | Haiku | 8 | 932 870 |
| 6 audit du correcteur | Sonnet | 1 | 114 978 |
| 7 index Graphify (extraction) | Haiku | 7 | 1 383 527 |
| **Total sous-agents** | | **42** | **6 419 228** |

Orchestrateur (Opus, session principale) : fenêtre de contexte à environ 470 000 jetons en fin de mission ; consommation exacte non exposée par l'outil. Forfait Max : 17 % du quota hebdomadaire tous modèles consommé à la fin de la phase de tests.

Tests (`claude plugin eval`, coût équivalent indiqué par l'outil) : 7 passages, 2,64 + 2,14 + 3,19 + 1,68 + 3,66 + 4,71 + 3,81 = **22,03 $** (sessions Sonnet et juge Sonnet, imputés sur le forfait Max, pas de dépense supplémentaire).

Rendement : les jetons Haiku (lecture, traduction, extraction Graphify) représentent 52 % du total sous-agents ; Opus n'a écrit aucun fichier volumineux (relectures, corrections ciblées, scripts, pilotage).

## 7. Réserves à rappeler à Jo

- **Avant toute commercialisation** : vérifier auprès de la DRH ou du référent déontologue les règles de cumul d'activités et les droits sur les œuvres créées par un agent public. Ce plan ne les a pas vérifiées. Conserver la preuve que le projet a été créé sur le temps personnel, avec des moyens personnels.
- **Protection** : un plugin fait de textes se copie facilement ; la licence PolyForm Noncommercial donne un fondement juridique, pas une protection technique.
- **Conditions de contribution** (`CONTRIBUTING.md`) : rédigées pour le projet, non relues par un juriste.
- **Nom** : un dépôt homonyme existe (`capybara114/pc-hardware-advisor`, site web, pas un plugin Claude) ; aucune recherche en registre de marques effectuée.
- **Publication publique** : non faite ; le dépôt reste privé tant que Jo ne demande pas l'inverse.
