# Passages 6 et 7 : 2026-11-07

## Passage 6 (cas 01, 03, 06, deux exécutions chacun) : 4,71 $, 663 s

Scores identiques sur les deux exécutions : 01 = 0,83 / 0,83 ; 03 = 0,50 / 0,50 ; 06 = 0,60 / 0,60. Correcteur « prices » en échec partout.
Audit par un juge indépendant (Sonnet, motifs cités) : échecs dus surtout à des types de vendeur « non confirmé » honnêtes (page sans ligne « vendu par »), à quelques prix en prose sans attributs, et, pour 06, à l'absence d'estimation des taxes d'import quand aucune page étrangère n'est lisible.
Corrections : correcteur aligné sur la règle d'honnêteté du plan (DECISIONS D20) ; `build-config` donne les coûts d'import applicables même sans page lue ; fourchettes de référence citées avec date, région et base.

## Passage 7 (complet, 7 cas) : 3,81 $, 414 s

| Cas | Score | Échecs | Constat |
|---|---|---|---|
| 01 | 0,83 | prices | Au seuil. |
| 02 | 1,00 | aucun | |
| 03 | 0,80 | prices | Au seuil pour la première fois. |
| 04 | 1,00 | aucun | |
| 05 | 0,25 | guardrails, history, schedule | Le bac à sable exposait cette fois un planificateur cloud (routines sur le compte) : le modèle a demandé confirmation avant de créer une tâche distante persistante. Historique créé. Prudence défendable, sanctionnée par le correcteur. |
| 06 | 0,60 | landed, prices | Jamais au seuil : sources d'import (Newegg, B&H) bloquées en 403, types de vendeur non affichés. |
| 07 | 0,50 | no-invention | Aucun skill du plugin déclenché (voulu) : réponse de Claude de base avec prix approximatifs, hors du contrôle du plugin. |

Boucle arrêtée après ce passage (voir REPORT.md §2).
