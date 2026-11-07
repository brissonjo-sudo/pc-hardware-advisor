# Passage 1 : 2026-11-07

`claude plugin eval . --eval-dir tests --ablation none -j 3 --judge-model sonnet`, sessions Sonnet, 1 exécution par cas. Coût : 2,64 $, 303 s.
Note préalable : un premier lancement n'a chargé aucun cas (deux-points non échappés dans le YAML des `prompt.md`) ; champs texte mis entre guillemets, YAML vérifié par script.

| Cas | Score | Correcteurs en échec | Diagnostic |
|---|---|---|---|
| 01 IA mini-ITX 14700KF | 0,83 | prices | Tableau sans date ni type de vendeur par ligne ; prix lus sur pages de recherche (vendeur non affiché). |
| 02 AM5 + kit XMP 7200 | 1,00 | aucun | Verdict « compatible sous condition » attendu, sources datées. |
| 03 Kit DDR5 meilleur prix | 0,30 | table, direct-only, prices | Lecture des seules pages de recherche (pas de ligne vendeur, pas de port), arrêt après 2 sources françaises, Europe quasi absente. |
| 04 Annonce RTX 3090 (ES) | 1,00 | aucun | Réponse en espagnol, verdict, tests, prix de marché sourcé. |
| 05 Suivi 3090 sous 800 € | 0,50 | schedule, history | Le skill demande confirmation alors que la demande contenait article, seuil et fréquence : rien créé en un tour. |
| 06 IA 32 Go, 2 000 € | 0,60 | landed, prices | Réponse honnête (budget irréaliste aux prix 2026), mais aucune option d'import chiffrée et tableau résumé sans date ni type par ligne. |
| 07 Hors périmètre | 1,00 | aucun | Refus poli, aucun skill déclenché, rien inventé. |

Score global 0,75 ; 4 cas sur 7 au seuil 0,8.

## Corrections apportées

1. `hunt-prices`, `search-playbook.md`, agent `price-scout` : pages de recherche = découverte seulement, lecture obligatoire de la fiche produit ; une page d'accueil, de recherche ou d'erreur ne compte pas comme source lue ; minimum 5 fiches produit de revendeurs directs distincts dans le pays de l'acheteur + 3 par zone supplémentaire demandée ; typage « direct retailer (site type; seller line not shown) » seulement pour un site listé comme direct sans marketplace, sinon groupe « Seller unconfirmed ».
2. `build-config` : chaque prix porte sur sa ligne date, vendeur, type, pays, prix rendu ou `excluding fees` ; au moins une option d'import chiffrée quand l'utilisateur l'accepte.
3. `track-price` : si la demande contient article, seuil et fréquence, appliquer les valeurs par défaut et agir, puis lister ces valeurs.
